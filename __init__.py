from anki.hooks import addHook
from .convert import translate


def populate_fields(editor):
    editor.saveNow(lambda: _populate_fields(editor))


def _populate_fields(editor):
    url = editor.note.fields[0]

    try:
        results = translate(url)
    except Exception as e:
        print(e)
        return

    note_name = editor.note.note_type()["name"]

    vals = results.get(note_name)

    if vals is None:
        print(f"Couldn't find results for note of type/name {note_name}")
        return

    for idx, val in enumerate(vals[:-1]):
        editor.note.fields[idx] = val
        editor.loadNote()

    for tag in vals[-1]:
        editor.note.add_tag(tag)

    editor.loadNote()


def add_auto_button(buttons, editor):
    auto_button = editor.addButton(
        icon=None,
        cmd="Pealim",
        func=populate_fields,
        tip="Download from Pealim",
        toggleable=False,
        label="",
        keys=None,
        disables=False,
    )
    buttons.append(auto_button)
    return buttons


addHook("setupEditorButtons", add_auto_button)
