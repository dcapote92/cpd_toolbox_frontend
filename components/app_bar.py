import flet as ft

def app_bar():

    def logout_check(e):

        def close_dialog(e):
            e.page.close(dialog)

        dialog = ft.AlertDialog(
            modal=True,
            title='Sair',
            content=ft.Text('Tem certeza que deseja sair da aplicação?'),
            actions_alignment=ft.MainAxisAlignment.END,
            actions=[
                ft.ElevatedButton(
                    icon=ft.Icons.EXIT_TO_APP,
                    bgcolor=ft.Colors.GREEN_600,
                    color=ft.Colors.WHITE,
                    on_click=lambda ev: [close_dialog(ev), ev.page.go('/login', replace=True)],
                    text='Confirmar'
                ),
                ft.ElevatedButton(
                    icon=ft.Icons.CANCEL,
                    bgcolor=ft.Colors.RED_600,
                    color=ft.Colors.WHITE,
                    on_click=close_dialog,
                    text='Cancelar'
                ),
            ]
        )

        e.page.open(dialog)

        

    return ft.AppBar(
        center_title=False,
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
        title=ft.Text('CPD ToolBox'),
        actions=[
            ft.IconButton(
                ft.Icons.HOME,
                tooltip='Principal',
                on_click= lambda e: e.page.go('/home')
            ),
            ft.IconButton(
                ft.Icons.LOGOUT,
                tooltip='Sair',
                on_click= logout_check
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