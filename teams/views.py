from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework.response import Response
from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError
from .models import Team
from utils import data_processing


class TeamsView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        teams_dict = []

        for team in teams:
            teams_convert = model_to_dict(team)
            teams_dict.append(teams_convert)
        return Response(teams_dict, status=200)

    def post(self, request: Request) -> Response:
        team_data = request.data
        try:
            data_processing(team_data)
        except (
            NegativeTitlesError,
            InvalidYearCupError,
            ImpossibleTitlesError,
        ) as error:
            return Response({"error": error.message}, status=400)

        teams_converse = Team.objects.create(**team_data)

        return Response(model_to_dict(teams_converse), 201)


class TeamsViewDetail(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team_data = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        team_dict = model_to_dict(team_data)
        return Response(team_dict, 200)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team_data = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        for k, v in request.data.items():
            setattr(team_data, k, v)
        team_data.save()
        return Response(model_to_dict(team_data), status=200)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team_data = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        team_data.delete()
        return Response(status=204)
