import os
import sys

from aqt import mw
from aqt.qt import (
    QAction,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QLineEdit,
    QVBoxLayout,
)
from aqt.utils import showInfo

addon_dir = os.path.dirname(__file__)
vendor_dir = os.path.join(addon_dir, "vendor")
if vendor_dir not in sys.path:
    sys.path.insert(0, vendor_dir)

from .convert import translate


action = QAction("Create Note from Pealim", mw)


class CreateNoteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Note")

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("https://www.pealim.com/dict/...")

        self.deck_combo = QComboBox(self)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Pealim URL:", self))
        layout.addWidget(self.url_input)
        layout.addWidget(QLabel("Deck:", self))
        layout.addWidget(self.deck_combo)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
            parent=self,
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def set_decks(self, decks, current_deck_id):
        self.deck_combo.clear()
        current_index = 0
        for idx, (name, deck_id) in enumerate(decks):
            self.deck_combo.addItem(name, deck_id)
            if deck_id == current_deck_id:
                current_index = idx
        self.deck_combo.setCurrentIndex(current_index)


def prompt_and_create_note():
    dialog = CreateNoteDialog(mw)
    decks = sorted(
        [(deck.name, deck.id) for deck in mw.col.decks.all_names_and_ids()],
        key=lambda d: d[0].lower(),
    )
    current_deck_id = mw.col.decks.current()["id"]
    dialog.set_decks(decks, current_deck_id)

    if dialog.exec() != QDialog.DialogCode.Accepted:
        return
    url = dialog.url_input.text().strip()
    if not url:
        return

    deck_id = dialog.deck_combo.currentData()

    try:
        results = translate(url)
    except Exception as e:
        showInfo(f"Translate failed: {e}")
        return

    if not results:
        showInfo("No results returned.")
        return

    missing_note_types = []
    for note_type_name, fields_and_tags in results.items():

        # print(f"{note_type_name}: {fields_and_tags}")

        note_type = mw.col.models.by_name(note_type_name)
        if note_type is None:
            missing_note_types.append(note_type_name)
            continue

        fields = fields_and_tags[:-1]
        tags = fields_and_tags[-1]

        note = mw.col.new_note(note_type)

        # print(f"note: {note.keys()} {note.fields}")

        for i, val in enumerate(fields):
            note.fields[i] = "" if val is None else str(val)

        if tags:
            note.tags.extend(tags)

        note.note_type()["did"] = deck_id

        mw.col.add_note(note, deck_id)

    if missing_note_types:
        showInfo(f"Missing note types: {', '.join(missing_note_types)}")
    mw.reset()


action.triggered.connect(prompt_and_create_note)

mw.form.menuTools.addAction(action)
