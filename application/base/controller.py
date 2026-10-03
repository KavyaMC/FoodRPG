from ..helpers.DataLoader import DataLoader
from .controls import (
    Button,
    ComboBox,
    Slider,
    TextArea,
    TextField,
    Toggle,
)
from .menu_manager import MenuManager
from .screen import Screen
from .state_object import StateObject


class Controller(StateObject):
    MENU_FILE = "menus.json"

    def __init__(self, state):
        super().__init__(state)

        self.screen = Screen(self.state)
        self.screen.controller = self

        self.menu_manager = MenuManager(self)
        self.data_loader = DataLoader()

    # Screen navigation

    def push(self, screen):
        self.screens.push(screen)

    def pop(self):
        self.screens.pop()

    def replace(self, screen):
        self.screens.replace(screen)

    def back(self):
        self.pop()

    # Menu navigation

    def add_menu(self, name, menu):
        self.menu_manager.add_menu(
            name,
            menu,
        )

    def open_menu(self, name):
        self.menu_manager.open(name)

    def back_menu(self):
        return self.menu_manager.back()

    @property
    def current_menu(self):
        return self.menu_manager.current

    def get_menu(self, name):
        data = self.data_loader.load(self.MENU_FILE)

        return data[name]

    def load_menu(self, menu):
        self.screen.title = menu.get(
            "title",
            "",
        )

        self.screen.description = menu.get(
            "description",
            "",
        )

        self.build_controls(
            menu.get(
                "items",
                [],
            )
        )

    # Control creation

    def create_control(self, item):
        match item["control"]:
            case "button":
                return self.create_button(item)

            case "toggle":
                return self.create_toggle(item)

            case "combo":
                return self.create_combo(item)

            case "slider":
                return self.create_slider(item)

            case "text":
                return self.create_text_field(item)

            case "text_area":
                return self.create_text_area(item)

            case _:
                raise ValueError(f"Unknown control type: {item['control']}")

    def create_button(self, item):
        action = item.get("action")
        submenu = item.get("submenu")

        if action and submenu:
            raise ValueError(f"'{item['label']}' cannot have both an action and a submenu.")

        if action:
            callback = getattr(
                self,
                action,
            )

            if "file" in item:
                return Button(
                    item["label"],
                    lambda: callback(item["file"]),
                )

            return Button(
                item["label"],
                callback,
            )

        if submenu:
            return Button(
                item["label"],
                lambda: self.open_menu(submenu),
            )

        raise ValueError(f"Button '{item['label']}' has no action or submenu.")

    def create_toggle(self, item):
        callback = None

        if item.get("on_changed"):
            callback = getattr(
                self,
                item["on_changed"],
            )

        return Toggle(
            item["label"],
            value=item.get(
                "value",
                False,
            ),
            on_changed=callback,
        )

    def create_combo(self, item):
        callback = None

        if item.get("on_changed"):
            callback = getattr(
                self,
                item["on_changed"],
            )

        return ComboBox(
            item["label"],
            options=item.get(
                "options",
                [],
            ),
            index=item.get(
                "index",
                0,
            ),
            on_changed=callback,
        )

    def create_slider(self, item):
        callback = None

        if item.get("on_changed"):
            callback = getattr(
                self,
                item["on_changed"],
            )

        return Slider(
            item["label"],
            value=item.get(
                "value",
                0,
            ),
            minimum=item.get(
                "minimum",
                0,
            ),
            maximum=item.get(
                "maximum",
                100,
            ),
            step=item.get(
                "step",
                1,
            ),
            on_changed=callback,
        )

    def create_text_field(self, item):
        callback = None

        if item.get("on_changed"):
            callback = getattr(
                self,
                item["on_changed"],
            )

        return TextField(
            item["label"],
            value=item.get(
                "value",
                "",
            ),
            placeholder=item.get(
                "placeholder",
                "",
            ),
            max_length=item.get(
                "max_length",
                64,
            ),
            on_changed=callback,
        )

    def create_text_area(self, item):
        return TextArea(
            item.get(
                "text",
                "",
            )
        )

    def build_controls(self, items):
        self.screen.clear_controls()

        for item in items:
            control = self.create_control(item)
            self.screen.add_control(control)

    # Controller lifecycle

    def update(self):
        pass

    def quit(self):
        self.game.quit()
