from genre.models import Genre
from genre.serializer import GenreSerializer
from rest_framework import serializers, status

from movie.models import Movie


class MovieSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField()
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    genre = GenreSerializer(many=True)

    def create(self, validated_data: dict):

        genres = validated_data.pop("genres")

        genre_data = [Genre.objects.get_or_create(**genre)[0] for genre in genres]

        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genre_data)

        return movie

    def update(self, genre_db, validated_data):

        for key, value in validated_data.items():

            if key == "genre":
                genre_data = [
                    Genre.objects.get_or_create(**genre)[0] for genre in value
                ]

                genre_db.genre.set(genre_data)
                continue

            setattr(genre_db, key, value)

        genre_db.save()

        return genre_db
