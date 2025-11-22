import flet as ft
from components.app_bar import app_bar


def create_home_view(page):

    # Função que será chamada ao clicar no botão, disparando a navegação
    def go_to_login(e):
        page.go("/login")
    
    def got_to_scales(e):
        page.go('/scales')

    return ft.View(
        route="/home",
        controls=[
            app_bar(),
            ft.Text("Bem-Vindo!"),
            ft.ElevatedButton("Sair", on_click=go_to_login),
            ft.ElevatedButton("Balanças", on_click=got_to_scales)
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )