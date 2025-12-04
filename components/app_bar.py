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

    def show_about(e):
        dlg_about = ft.AlertDialog(
            modal=True,
            title='Sobre...',
            content=ft.Text('CPD ToolBox, é um projeto pessoal que segue a' \
            ' ideia de manter todas as ferramentas necessarias para ' \
            'um CPD centralizadas e facilmente acessíveis'),
            actions=[
                ft.TextButton('Fechar',
                              ft.Icons.CLOSE,
                              icon_color=ft.Colors.WHITE,
                              style=ft.ButtonStyle(bgcolor=ft.Colors.RED_600, color=ft.Colors.WHITE),
                              autofocus=True,
                              on_click=lambda e: e.page.close(dlg_about)
                              )
            ],
            action_button_padding=10,
            actions_alignment=ft.MainAxisAlignment.END
        )
        e.page.open(dlg_about)
        

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
                ft.Icons.INFO,
                tooltip='Sobre',
                on_click=show_about
            ),
            ft.IconButton(
                ft.Icons.LOGOUT,
                tooltip='Sair',
                on_click= logout_check
            )
        ]
    )