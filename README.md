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

**Branch** - Do inglês "ramo" é um ramo de trabalho, é o local em que cada integrante irá trabalhar. Para toda unidade de trabalho nova, deve-se criar uma branch, caso não exista uma.

**Pull** - Do inglês "puxar" é a ação de obter as últimas atualizações de uma branch, caso haja alguma. (Como se estivesse atualizando um aplicativo).

**Push** - Do inglês "empurrar" é a ação de enviar as atualizações locais para uma branch. (Como se estivesse criando uma atualização).

São os termos que mais irão encontrar.

<h1>Fluxo de trabalho</h1>

Primeiramente, certifiquem-se que a SDK do git está instalada (nota: Não é GitDesktop Ou GitLab, ou qualquer software gerenciador, é apenas GIT).

Extensão de git do VsCode também seria interessante, mas opcional, caso vão usar VsCode.


<h2>Setup inicial</h2>

"Estou em uma pasta vazia, e agora?"

- Vá até a página desse repositório, clique na branch **main** e procure por um botão verde, lá vai ter as opções de *git glone*, você pode baixar o .zip e descompactar, ou você pode copiar o código que vai aparecer e colar na janela de comando.

- Caso não tenha feito, o VsCode (Ou outra IDE) vai pedir em algum momento para você se logar na sua conta.

- Para saber se foi tudo certinho, cheque se os arquivos na sua pasta são exatamente os mesmos da branch.

- Após isso, garanta que o python 3.12 ou superior está instalado. Abra um prompt da sua IDE ou cmd do windows e vá até a raíz do projeto, crie uma virtual env com o comando: *python -m venv .windows_env*. 
- Então, ative o env com o comando: ".\.windows_env\Scripts\activate". Ou vá até a pasta .windows_env\Scripts e execute o arquivo "activate.bat"
- Por fim, instale as dependências do projeto com: *pip install -r requirements.txt*

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

**- ERRO COMUM DE DEV. CERTIFIQUE-SE DE QUE VOCÊ ESTÁ FAZENDO ALTERAÇÕES NA BRANCH CERTA, POIS MIGRAR AS ALTERAÇÕES PODE SER UMA DOR DE CABEÇA. E corre-se o risco de perder seu trabalho.**

Aproveitando: **NÃO ALTERE A BRANCH MAIN EM NENHUMA CIRCUNSTÂNCIA.** Inclusive, vou colocar uma proibição para que não seja permitido de qualquer forma, para evitar acidentes.

<h2> Onde eu trabalho? </h2>
- Vá até o respectivo arquivo e a respectiva classe que você irá implementar e sobrescreva os métodos que possuem "iterative" ou "recursive" no nome. Você pode fazer qualquer coisa com a classe desde que consiga implementar o algoritmo e desde que mantenha o uso daqueles métodos. Os métodos não precisam retornar nenhum valor.

<h2>Terminando o trabalho</h2>

"Quero salvar as alterações, e agora?"
- Faça o comando "git add ." para adicionar todos os arquivos em um novo commit.
- Faça "git commit -m *mensagem-do-commit*", similar à branch, evite nomes muito longos e descreva exatamente a alteração que você fez.

**Nota, você pode e deve fazer quantos commits quiser! Pense que é o botão "salvar" de um jogo. Sempre que fizer uma alteração que considere importante, faça esses dois comandos!**

- Por fim, faça git push. Caso seja seu primeiro push, ele irá falhar e o git vai falar que não há branch remota correspondete, e vai te dar um comando para isso. Caso não dê o comando, faça "git push --set-upstream origin *nome-da-sua-branch*" **IMPORTANTE! CERTIFIQUE-SE DE QUE A BRANCH REMOTA TENHA O MESMO NOME DA LOCAL, PRA EVITAR CONFUSÃO**.

- Após finalizar, verifique o site do github, neste repositório, e veja se sua branch apareceu e seus arquivos ali.

<h3>Mesclando o trabalho final</h3>

- Após finalizar tudo de sua parte, você vai ir na página desse repositório e vai criar uma **PULL REQUEST** da sua branch. *"O que é uma pull request?"*: É basicamente um pedido para mesclar a sua branch com outra, como se você fosse encaixar uma peça no quebra cabeça.
- Crie ela com um nome descritivo e coloque para mesclar na branch **main**. A partir daí, eu poderei verificar o código e ver se está apto.
