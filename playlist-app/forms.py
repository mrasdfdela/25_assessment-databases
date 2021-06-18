"""Forms for playlist app."""

from wtforms import SelectField, TextField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = TextField("Name", validators=[InputRequired()])
    description = TextField("Description")
    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = TextField("Title", validators=[InputRequired()])
    artist = TextField("Artist", validators=[InputRequired()])

    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
