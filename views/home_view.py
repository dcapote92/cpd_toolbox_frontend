import flet as ft
from components.app_bar import app_bar

def create_home_view(page: ft.Page):
    
    content = ft.Column(
        controls=[
            ft.Text("Bem-vindo ao CPD ToolBox!", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("Selecione uma opção abaixo:", size=16),
            ft.Divider(),
            ft.ElevatedButton(
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    padding=0
                ),
                on_click= lambda _: page.go('/scales'),
                width=200,
                height=200,
                content=ft.Column(
                    controls=[
                        ft.Icon(
                            name=ft.Icons.SCALE,
                            size=60,
                            #color=ft.Colors.BLUE_700
                        ),
                        ft.Text(
                            value='Gerir Balanças',
                            size=25,
                            weight=ft.FontWeight.BOLD
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                )
            )
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    return ft.View(
        route='/home', 
        controls=[
            app_bar(), 
            ft.Container(
                content=content,
                padding=20,
                alignment=ft.alignment.top_center
            )
        ],
        bgcolor=ft.Colors.WHITE,
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )