# 🎒 Preparando o seu equipamento

Antes da primeira missão, você precisa de quatro ferramentas. O guia principal é para **Windows com o VS Code**; as dicas de **Mac** e **Linux** aparecem nos quadros marcados com 🍎 e 🐧.

| Ferramenta | Para quê | Versão |
|---|---|---|
| **VS Code** | escrever e rodar o código | a mais recente |
| **Python** | níveis 1, 3 e 5 (e o placar do jogo) | 3.10 ou mais novo |
| **Node.js** | níveis 2, 4 e 6 (JavaScript e TypeScript) | 22.18 ou mais novo (LTS) |
| **Git** | guardar o progresso e entregar no GitHub | qualquer versão recente |

No fim, o comando `python quest.py ambiente` confere tudo para você. ✅

---

## 1. VS Code

1. Baixe em https://code.visualstudio.com e instale.
2. Abra o VS Code, clique no ícone de **Extensões** (quadradinhos, `Ctrl+Shift+X`) e instale **Python** (da Microsoft). Ele deve aparecer como recomendado quando você abrir a pasta do jogo.
3. Dica: para ler os arquivos `LEIAME.md` formatados, abra o arquivo e use `Ctrl+Shift+V` (visualização do Markdown).

## 2. Python

1. Baixe em https://www.python.org/downloads (3.10 ou mais novo).
2. **Na primeira tela do instalador, marque "Add python.exe to PATH"** e clique em *Install Now*.
3. Abra o terminal do VS Code (`` Ctrl+` ``) e confira:
   ```
   python --version
   ```
   - Se abrir a Microsoft Store ou der erro, tente `py --version` (e use `py` no lugar de `python` nos comandos).
   - Se acabou de instalar e o comando não é reconhecido, **feche e abra o VS Code de novo**.

> 🍎 **Mac:** `brew install python` (ou instale pelo site). No Mac o comando é `python3` (use `python3 quest.py`).
> 🐧 **Linux (Ubuntu/Debian):** `sudo apt install python3 git`. Use `python3 quest.py`.

## 3. Node.js

1. Baixe a versão **LTS** em https://nodejs.org e instale com as opções padrão.
2. Feche e abra o VS Code e confira:
   ```
   node --version
   ```
   Precisa mostrar **v22.18 ou mais novo** para usar TypeScript direto. Com uma versão entre 20.11 e 22.17 você ainda joga em **JavaScript**.

> 🍎 **Mac:** `brew install node`.
> 🐧 **Linux:** o `nodejs` do apt costuma ser antigo. Prefira o **nvm** (https://github.com/nvm-sh/nvm): `nvm install --lts`.

## 4. Git e GitHub

1. Instale o Git em https://git-scm.com (no Windows, as opções padrão servem).
2. Configure o seu nome e e-mail, **uma vez**:
   ```
   git config --global user.name "Seu Nome"
   git config --global user.email "seu-email@exemplo.com"
   ```
3. Crie uma conta gratuita em https://github.com (se ainda não tiver).
4. No VS Code, clique no ícone de **Contas** (canto inferior esquerdo) e escolha **Entrar com o GitHub**. Isso evita pedir senha a cada `push`.

> 🍎 **Mac:** o `git` vem com as ferramentas de linha de comando da Apple; se o Mac oferecer instalá-las, aceite.
> 🐧 **Linux:** `sudo apt install git`.

---

## 5. Criando o seu repositório da missão

1. Abra a página do jogo no GitHub (https://github.com/juniorbsn-ui/jornada-funcional) e clique em **Use this template → Create a new repository**.
2. Dê o nome `lpp-quest-SUA_MATRICULA` e crie.
3. No VS Code, aperte `Ctrl+Shift+P`, digite **Git: Clone**, cole a URL do **seu** repositório e escolha uma pasta. Abra a pasta quando o VS Code perguntar.
4. Compartilhe o repositório com o professor, como indicado no `README.md`.

## 6. Jogando

No terminal do VS Code (`` Ctrl+` ``), dentro da pasta do jogo:

```
python quest.py ambiente     # confere o equipamento
python quest.py              # roda todos os níveis e mostra o placar
python quest.py 1            # detalhes do nível 1
```

Atalho: `Ctrl+Shift+B` roda **⚔️ Jogar (todos os níveis)** sem digitar nada.

Quer usar **TypeScript** nos níveis de Node? Rode `python quest.py escolher ts` uma vez. Para voltar ao JavaScript, `python quest.py escolher js`.

## 7. Salvando e entregando o progresso

A cada missão ou nível concluído:

```
git add .
git commit -m "nivel 1: vila do boletim concluida"
git push
```

No VS Code também dá: aba **Controle do Código-Fonte** (`Ctrl+Shift+G`), escreva a mensagem, clique em **Confirmar** e depois em **Sincronizar**.

---

## 🛠️ Deu problema?

| Sintoma | O que fazer |
|---|---|
| `python` não é reconhecido | Feche e abra o VS Code; tente `py`; reinstale o Python marcando **Add to PATH** |
| `node` não é reconhecido | Feche e abra o VS Code; reinstale o Node LTS |
| O placar mostra `⚠️ seu Node é antigo demais` | Atualize o Node (LTS), ou use apenas JavaScript com Node 20.11+ |
| TypeScript não roda | Precisa do Node 22.18+; confira com `node --version` ou use JavaScript |
| Os emojis aparecem como `?` | Use o terminal do VS Code ou o Windows Terminal |
| O `git push` pede senha | Entre com o GitHub no VS Code (Contas) ou use um token de acesso pessoal |
| O placar não muda depois que eu editei | Salve o arquivo (`Ctrl+S`) antes de rodar `python quest.py` |
