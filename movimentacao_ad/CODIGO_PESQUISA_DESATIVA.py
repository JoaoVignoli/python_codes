import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, colors
from ldap3 import Server, Connection, SUBTREE, MODIFY_REPLACE


def main(page: Page):
    page.title = "MOVIMENTAÇÕES AD"

    print("Initial route:", page.route)

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("UNIFIQUE")),
                    ft.Text("MOVIMENTAÇÕES AD"),
                    ft.Text("Escolha seu usuário:"),
                    dropdown_user,
                    ElevatedButton("LOGIN", on_click=open_options),
                ],
            )
        )
        if page.route == "/options" or page.route == "/options/newhost" or page.route == "/options/move" or page.route == "/options/disable":
            page.views.append(
                View(
                    "/options",
                    [
                        AppBar(title=Text("Options"), bgcolor=colors.SURFACE_VARIANT),
                        Text(f"Seja bem vindo {dropdown_user.value}! Escolha o que deseja fazer:", style="bodyMedium"),
                        ElevatedButton(
                            "HOST UTILIZADOS", on_click=open_options_newhost 
                        ),
                        ElevatedButton(
                            "MOVER", on_click=open_options_move
                        ),
                        ElevatedButton(
                            "DESATIVAR", on_click=open_options_disable
                        ),
                    ],
                )
            )
        if page.route == "/options/newhost":
            page.views.append(
                View(
                    "/options/newhost",
                    [
                        AppBar(
                            title=Text("HOST UTILIZADOS"), bgcolor=colors.SURFACE_VARIANT
                        ),
                        Text("Selecione a cidade que deseja:"),
                        dropdown_city,
                        Search_btn,
                        lv,
                    ],
                )
            )
        if page.route == "/options/move":
            page.views.append(
                View(
                    "/options/move",
                    [
                       AppBar(
                            title=Text("MOVIMENTAR"), bgcolor=colors.SURFACE_VARIANT
                        ),
                        Text("Qual maquina deseja movimentar?"), 
                    ]
                )
            )
        if page.route == "/options/disable":
            page.views.append(
                View(
                    "/options/disable",
                    [
                       AppBar(
                            title=Text("DESABILITAR"), bgcolor=colors.SURFACE_VARIANT
                        ),
                        Text("Escreva o nome da maquina que deseja desabilitar:"), 
                        Host_Disable,
                        Disable_btn,
                        hd1,
                        hd2,
                        hd3,
                    ]
                )
            )
        page.update()



    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_options_disable(e):
        Host_Disable.value = ""
        hd1.value = ""
        hd2.value = ""
        hd3.value = ""
        page.go("/options/disable")

    def open_options_move(e):
        page.go("/options/move")
    
    def open_options_newhost(e):
        dropdown_city.value = ""
        page.go("/options/newhost")
        lv.clean()

    def open_options(e):
        page.go("/options")

    def Search_Host(e):
        lv.clean()
        page.clean()
        # Configurações de conexão
        server = Server('10.252.192.11')  # Substitua pelo endereço do servidor AD
        username = ''  # Substitua pelo nome de usuário com permissões no AD
        password = ""  # Substitua pela senha do usuário

        # Conectar ao servidor AD
        conn = Connection(server, user=username, password=password)

        if not conn.bind():
            print('Falha na autenticação')
            exit()

        # Exemplo: consultar usuários
        conn.search(
            search_base='DC=redeunifique,DC=com,DC=br',  # Substitua pelo seu domínio AD
            search_filter='(&(objectClass=computer)(cn=*UNI-' + dropdown_city.value +'*))',
            search_scope=SUBTREE,
            attributes=['cn']  # Atributos a serem recuperados
        )

        HostResult = []

        for entry in conn.entries:
            cn = entry.cn.value  # Obter o valor do atributo CN
            HostResult.append(cn.upper())

        HostResult.sort(reverse=True)

        # Imprimir os CNs dos hosts
        for host in HostResult:
            lv.controls.append(ft.Text(f"Hostname {host}"))
        # Encerrar a conexão
            conn.unbind()
            page.update()
    lv = ft.ListView(height=300, spacing=10)

    
    def Disable_Host(e):
        page.clean
        server = Server('10.252.192.11')  # Substitua pelo endereço do servidor AD
        username = 'guaca.infran1@redeunifique.com.br'  # Substitua pelo nome de usuário com permissões no AD
        password = "USH)Z<4%HzaNp@'s_a^/"  # Substitua pela senha do usuário

        # Conectar ao servidor AD
        conn = Connection(server, user=username, password=password)

        if not conn.bind():
            print('Falha na autenticação')
            exit()

        # Exemplo: consultar usuários
        conn.search(
        search_base='DC=redeunifique,DC=com,DC=br',  # Substitua pelo seu domínio AD
        search_filter='(&(objectClass=computer)(cn=' + Host_Disable.value + '))',
        search_scope=SUBTREE,
        attributes=['cn', 'distinguishedName', 'userAccountControl' ]  # Atributos a serem recuperados
    )
        
        Disable_ID = '4098'
        HostResult = None  # Inicialize a variável com None
        modification = {'userAccountControl': [(MODIFY_REPLACE, ['4098'])]
                        }
        for entry in conn.entries:
            cn = entry.cn.value  # Obter o valor do atributo CN
            dn = entry.distinguishedName.value
            uac = entry.userAccountControl.value
            if cn is not None:
                HostResult = cn
                HostPlace = dn
                HostControl = f"{uac}"
            if HostControl == Disable_ID:
                hd1.value = ""
                hd3.value = ""
                hd2.value= f"{HostResult} já está desabilitado no AD"
            else:
                conn.modify(HostPlace, modification)
                hd3.value = ""
                hd2.value = ""
                hd1.value = f"{HostResult} localizado e desabilitado no AD"
            break

        if HostResult is None:
            hd1.value = ""
            hd2.value = ""
            hd3.value = (f"{Host_Disable.value} não localizado no AD")
        page.update()
        conn.unbind()
    hd1 = Text()
    hd2 = Text()
    hd3 = Text()

    Disable_btn = ft.ElevatedButton(
        text="Desabilitar", on_click=Disable_Host
    ) 

    Search_btn = ft.ElevatedButton(
         text="Pesquisar", on_click=Search_Host
    )
     
    dropdown_user = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("joao.vignoli"),
            ft.dropdown.Option("luan.boimler"),
            ft.dropdown.Option("tiago.busnardo"),
        ],
    )

    dropdown_city = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("TIO"),
            ft.dropdown.Option("BNU"),
            ft.dropdown.Option("GUB"),
        ],
    )

    Host_Disable = ft.TextField(label="Hostname")
    
    page.go(page.route)


ft.app(port=56765,target=main, view=ft.WEB_BROWSER)
