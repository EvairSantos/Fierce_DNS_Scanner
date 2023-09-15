<h1>Fierce DNS Scanner</h1>
O Fierce DNS Scanner é uma ferramenta Python simples e poderosa para realizar escaneamento e busca DNS em um domínio específico. Ele foi projetado para ajudar os administradores de sistemas, pentesters e entusiastas da segurança a coletar informações sobre um domínio-alvo, incluindo registros DNS, servidores de nomes autoritativos e registros de recursos comuns.
Recursos Principais

    Busca de Servidores de Nomes Autoritativos: O Fierce DNS Scanner começa pesquisando os servidores de nomes autoritativos do domínio-alvo, fornecendo informações importantes para a próxima fase da análise.

    Transferência de Zona: A ferramenta tenta realizar uma transferência de zona para o domínio, se possível, a fim de obter um instantâneo completo dos registros DNS do domínio. Isso pode revelar informações valiosas.

    Busca DNS por Força Bruta: Se a transferência de zona não for bem-sucedida, o Fierce DNS Scanner pode executar uma busca DNS por força bruta, consultando servidores de nomes autoritativos em busca de registros DNS comuns, como subdomínios conhecidos.

    Saída Personalizável: Os resultados podem ser salvos em um arquivo de saída personalizado ou exibidos na tela.

<h1>Como Usar</h1>

    Execute o script e insira o domínio que deseja escanear quando solicitado.

    Você pode opcionalmente especificar um arquivo de saída para salvar os resultados usando a opção -o ou --output.

    A ferramenta primeiro tentará realizar uma transferência de zona. Se bem-sucedida, ela exibirá os resultados. Caso contrário, ela executará uma busca DNS por força bruta.

    Os resultados são exibidos na tela ou salvos no arquivo de saída especificado.

<h1>Requisitos</h1>

    Python 3.x
    Biblioteca dnspython

Configuração

Certifique-se de ter instalado a biblioteca dnspython antes de usar o Fierce DNS Scanner. Você pode instalá-la usando o pip:

bash

pip install dnspython

<h1>Contribuição</h1>

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e solicitações de pull (pull requests) para melhorar esta ferramenta.

<h1>Aviso Legal</h1>
Este software é fornecido apenas para fins educacionais e de teste. O uso indevido ou não autorizado desta ferramenta pode violar as leis de privacidade e segurança. O autor não assume qualquer responsabilidade pelo uso indevido desta ferramenta.

<h1>Licença</h1>
Este projeto é licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

Espero que esta descrição ajude a destacar as principais funcionalidades e finalidades da sua ferramenta no GitHub. Lembre-se de manter o README atualizado à medida que você faz alterações ou melhorias no projeto.
