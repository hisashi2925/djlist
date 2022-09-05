from sys import implementation
from unicodedata import category
from django.contrib import admin
from .models import Djdata
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.fields import Field

class DjmaxMusicResource(resources.ModelResource):
    music_name = Field(attribute="music_name", column_name="曲名")
    pack = Field(attribute="pack", column_name="PACK")
    category = Field(attribute="category", column_name="カテゴリ")
    artist = Field(attribute="artist", column_name="アーティスト")
    bpm = Field(attribute="bpm", column_name="BPM")
    implementation_date = Field(attribute="implementation_date", column_name="実装日")
    key_4n = Field(attribute="key_4n", column_name="4N")
    key_4h = Field(attribute="key_4h", column_name="4H")
    key_4m = Field(attribute="key_4m", column_name="4M")
    key_4s = Field(attribute="key_4s", column_name="4S")
    key_5n = Field(attribute="key_5n", column_name="5N")
    key_5h = Field(attribute="key_5h", column_name="5H")
    key_5m = Field(attribute="key_5m", column_name="5M")
    key_5s = Field(attribute="key_5s", column_name="5S")
    key_6n = Field(attribute="key_6n", column_name="6N")
    key_6h = Field(attribute="key_6h", column_name="6H")
    key_6m = Field(attribute="key_6m", column_name="6M")
    key_6s = Field(attribute="key_6s", column_name="6S")
    key_8n = Field(attribute="key_8n", column_name="8N")
    key_8h = Field(attribute="key_8h", column_name="8H")
    key_8m = Field(attribute="key_8m", column_name="8M")
    key_8s= Field(attribute="key_8s", column_name="8S")
    remarks = Field(attribute="remarks", column_name="備考")
    
    class Meta:
        model = Djdata
        skip_unchanged = True
        use_bulk = True

@admin.register(Djdata)

class DjmaxDataAdmin(ImportExportActionModelAdmin):
    ordering = ["music_name"]
    list_display = (
        "music_name",
        "pack",
        "category",
        "artist",
        "bpm",
        "implementation_date",
        "key_4n",
        "key_4h",
        "key_4m",
        "key_4s",
        "key_5n",
        "key_5h",
        "key_5m",
        "key_5s",
        "key_6n",
        "key_6h",
        "key_6m",
        "key_6s",
        "key_8n",
        "key_8h",
        "key_8m",
        "key_8s"

    )
    resource_class = DjmaxMusicResource
