# 🛡️ lab-git-donola - Blue Team Lab

Laboratório prático de Git com foco em Segurança da Informação e resposta a incidentes.

## 🎯 Objetivos do Lab
- Dominar o fluxo Git: `init`, `add`, `commit`, `branch`, `merge`
- Simular vazamento de credencial e remediação com `git revert`
- Recuperar histórico perdido usando `git reflog`
- Sanitizar repositório remoto com `git push --force`

## 🚨 Incidente Simulado
Neste lab foi simulado um commit contendo dados sensíveis:
1. **Detecção**: Senha exposta no arquivo `SOC.md`
2. **Contenção**: Reversão via `git revert 63c40ca`
3. **Erradicação**: `git reset --hard` para commit seguro
4. **Recuperação**: `git push -f` para limpar histórico remoto

## 📚 Comandos Dominados
`git status` | `git log` | `git diff` | `git branch` | `git checkout` | `git merge` | `git revert` | `git reflog` | `git reset` | `git push -f`

## 🔵 Stack
Git | GitHub | Blue Team | Incident Response

---
**Autor:** Donolaxp  
**Status:** Lab concluído com sucesso ✅

markdown# 🛡️ Blue Team Lab - DonolaXP

Detector de tentativas de Brute Force em logs SSH usando Python.

## 🚨 O que faz?
Analisa arquivos de log e alerta sobre tentativas de invasão via SSH.

## ⚙️ Como rodar
```bash
python analisa_log.py📊 Exemplo de Saídajavascript🚨 ALERTA: Failed password for root from 192.168.1.100
📊 Total de tentativas de invasão detectadas: 2
⚠️ NÍVEL ATENÇÃO! Monitorar IPs suspeitos.🎯 Skills Demonstradas
Python para automação Blue TeamAnálise de logs de segurança  Git e GitHub para versionamentoBoas práticas: .gitignore para proteger credenciais👨‍💻 Autor
Felipe Donola - Futuro Analista de SOC

