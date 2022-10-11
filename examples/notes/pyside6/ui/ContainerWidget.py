from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QLabel

from core.globalstate import GlobalState
from core.observer import Observer
from examples.notes.action.add_note import AddNote


class ContainerWidget(
    QWidget,
    Observer,
    metaclass=type(
        'QWidgetObserver',
        (type(QWidget), type(Observer)),
        {}
    )
):
    def __init__(self):
        QWidget.__init__(self)
        self.observe(GlobalState.get('notes').notes)
        self.setLayout(QVBoxLayout(self))

        self.notes_list = QWidget()
        self.notes_list.setLayout(QVBoxLayout(self.notes_list))
        self.notes_list.layout().setAlignment(Qt.AlignTop)
        self.lineedit = QLineEdit()

        self.lineedit.returnPressed.connect(self.handle_return_pressed_lineedit)

        self.layout().addWidget(self.notes_list)
        self.layout().addWidget(self.lineedit)

    def handle_return_pressed_lineedit(self):
        note = self.lineedit.text()
        GlobalState.get('notes').add_note(note)

    def notify_state_changed(self, action):
        if isinstance(action, AddNote):
            self.notes_list.layout().addWidget(QLabel(text=action.note))
            self.lineedit.setText('')
