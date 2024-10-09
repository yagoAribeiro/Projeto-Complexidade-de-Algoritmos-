# Projeto-Complexidade-de-Algoritmos-
Projeto em grupo da disciplina de Complexidade de Algoritmos, do curso de ciência da computação.

Integrantes:
Yago Amâncio Ribeiro.
Juan Carlos Barbosa.
Leandro Oliveira
Paulo Henrique Alvez
Gabriel Bonfim

Para os integrantes:

<h1>Sobre o Git</h1>

Nota-se que não sou experiente com git, tenho conhecimento do básico, qualquer problema que fuja desse guia, podemos rever em particular.

O básico de Git que você deverá saber:

<h2>Definições importantes</h2>

**Branch** - Do português "ramo" é um ramo de trabalho, é o local em que cada integrante irá trabalhar. Para toda unidade de trabalho nova, deve-se criar uma branch, caso não exista uma.

**Pull** - Do português "puxar" é a ação de obter as últimas atualizações de uma branch, caso haja alguma. (Como se estivesse atualizando um aplicativo).

**Push** - Do português "empurrar" é a ação de enviar as atualizações locais para uma branch. (Como se estivesse criando uma atualização).

São os termos que mais irão encontrar.

<h1>Fluxo de trabalho</h1>

Primeiramente, certifiquem-se que a SDK do git está instalada (nota: Não é GitDesktop Ou GitLab, ou qualquer software gerenciador, é apenas GIT).

Extensão de git do VsCode também seria interessante, mas opcional, caso vão usar VsCode.


<h2>Setup inicial</h2>

"Estou em uma pasta vazia, e agora?"

- Vá até a página desse repositório, clique na branch **main** e procure por um botão verde, lá vai ter as opções de *git glone*, você pode baixar o .zip e descompactar, ou você pode copiar o código que vai aparecer e colar na janela de comando.

- Caso não tenha feito, o VsCode (Ou outra IDE) vai pedir em algum momento para você se logar na sua conta.

- Para saber se foi tudo certinho, cheque se os arquivos na sua pasta são exatamente os mesmos da branch. Caso sejam, a configuração está completa.

<h2>Começando o trabalho</h2>
"E agora?"
- Primeiramente, sempre que for criar uma branch nova, atualize a branch *main*, para apurar atualizações importantes.

"Como vejo se estou na branch correta?"
- Na janela de comando, use "git branch" para listar as branches na sua pasta. Dependendo da IDE, a branch selecionada vai ter uma cor diferente ou asterisco.
  
"Como seleciono a branch?" 
- Use "git checkout *nome-branch*". Cuidado, isso irá mudar os arquivos da sua pasta, dependendo, o git irá pedir para você fazer alguns comandos, e então você segue.

"A branch que eu quero não está aparecendo com git branch!"
- Vá até a página deste repositório e procure a branch que você quer, copie o nome e dê *git checkout* no nome dela. Ele irá copiar do remoto.

**- Suas branches da pasta são locais e não atualizam sozinhas! Sempre que der um checkout, faça "git pull", para atualizar sua branch.**

- Selecione a branch **main** e faça *pull*, antes de criar uma nova.

- Crie uma branch com um nome descritivo de o que você irá fazer, não faça nomes muito longos. Use "git branch *nome-branch-nova*" para criar uma nova baseada na selecionada.

- Por fim, selecione a branch nova que acabou de criar, usando aquele comando do *git checkout* mostrado anteriormente. Agora você está pronto para fazer o que seu coração mandar.

**- ERRO COMUM DE DEV. CERTIFIQUE-SE DE QUE VOCÊ ESTÁ FAZENDO ALTERAÇÕES NA BRANCH CERTA, POIS MIGRAS AS ALTERAÇÕES PODE SER UMA DOR DE CABEÇA. E corre-se o risco de perder seu trabalho.**

Aproveitando: **NÃO ALTERE A BRANCH MAIN EM NENHUMA CIRCUNSTÂNCIA.** Inclusive, vou colocar uma proibição para que não seja permitido de qualquer forma, para evitar acidentes.
