import flet as ft
from components.search_bar import SearchBar
def app_bar():

    return ft.AppBar(
        center_title=False,
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
        actions=[
            ft.IconButton(
                ft.Icons.LOGOUT,
                tooltip='Sair',
                on_click= lambda e: print('Sair foi clicado')
            ),
            ft.PopupMenuButton(
                icon=ft.Icons.MENU,
                items=[
                    ft.PopupMenuItem(
                        text='Configurações',
                        icon=ft.Icons.SETTINGS,
                        on_click=lambda e: print('Clicado Settings'),
                        data="Configurações"
                    ),
                    ft.PopupMenuItem(
                        text='Sobre',
                        icon=ft.Icons.INFO,
                        on_click=lambda e: print('Clicado Sobre'),
                        data="Sobre"
                    ),
                ],
                tooltip='Menu'
            )
        ]
    )