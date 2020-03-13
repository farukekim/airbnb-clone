from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ ItemAdmin Definition """

    list_display = (
        "name", "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ RoomAdmin Definition """

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": ("name", "description", "country", "address", "price")
            }
        ),
        (
            "Times",
            {
                "fields": ("check_in", "check_out", "instant_book")
            }
        ),
        (
            "Spaces",
            {
                "fields": ("guests", "beds", "bedrooms", "baths")
            }
        ),
        (
            "More About the Spaces",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules")
            }
        ),
        (
            "Last Details",
            {
                "fields": ("host",)
            }
        ),

    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
    "host__superhost", "instant_book", "room_type", "amenities", "facilities", "house_rules", "city", "country")
    search_fields = ("=city", "^host__username")
    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ PhotoAdmin Definition """
    pass
