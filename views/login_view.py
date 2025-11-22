import flet as ft
from components.app_bar import app_bar
import resources


def create_login_view(page: ft.Page):
    
    def login(e):
        page.go('/home')

    def register(e):
        page.go('/register')

    img_logo = ft.Image(
        src='resources/logo.img',
        width=200,
        height=80
    )

    edt_user = ft.TextField(
        keyboard_type=ft.KeyboardType.NAME,
        multiline=False,
        max_length=15,
        label='Usuário',
        enable_suggestions=True,
        autofocus=True
    )
    
    edt_password = ft.TextField(
        keyboard_type=ft.KeyboardType.NAME,
        multiline=False,
        max_length=15,
        label='Senha',
        autofocus=True,
        password=True,
        can_reveal_password=True
    )

    btn_login = ft.ElevatedButton(
        text='Entrar',
        icon= ft.Icons.LOGIN,
        width=120,
        on_click=lambda e: print(f'Botão {btn_login.text} apertado')
    )

    btn_register = ft.ElevatedButton(
        text='Registrar',
        icon= ft.Icons.APP_REGISTRATION,
        width=120,
        on_click=lambda e: print(f'Botão {btn_register.text} apertado')
    )

    rw_buttons = ft.Row(
        controls=[
            btn_login,
            btn_register
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    box_container = ft.Container(
        height=500,
        width=400,
        border=ft.border.all(width=3, color=ft.Colors.BLUE_GREY_500),
        border_radius=ft.border_radius.all(10),
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                edt_user,
                edt_password,
                rw_buttons
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=20,
    )

 

    return ft.View(
        route='/login',
        controls=[
            img_logo,
            box_container,
            ft.Text('©2025 Daniel Capote')
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
