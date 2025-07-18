# 🤖 Claude Code - Instruções de Sessão para Repositório MAV

## Prompt Inicial para Novas Sessões

Use este prompt ao iniciar uma nova sessão no VS Code com Claude Code:

```
Olá! Estou trabalhando no repositório MAV (Máquina Automática de Vendas) que contém:

1. Uma base de conhecimento estruturada sobre marketing digital e funis de conversão
2. Módulos teóricos (M1-M7) em /modules/
3. Exercícios práticos em /exercises/ 
4. Prompts para IA em /materials/
5. Biblioteca de referência com 4 livros convertidos para Markdown em /references/:
   - DotCom Secrets, Expert Secrets, Traffic Secrets (Russell Brunson)
   - Copywriting Secrets (Jim Edwards)

Por favor:
- Leia o arquivo /docs/project-memory.md para contexto completo
- Verifique o PLANO_OTIMIZACAO_KB.md para roadmap do projeto
- Consulte o README.md principal para estrutura atual

Última sessão realizamos: conversão dos livros para Markdown com PyMuPDF4LLM.

Como posso ajudar hoje com o projeto MAV?
```

## Contexto Importante para Claude

### Estrutura do Repositório
```
mav/
├── modules/         # Teoria dos módulos M1-M7
├── exercises/       # Exercícios práticos
├── materials/       # Prompts para IA
├── references/      # Livros Russell Brunson e Jim Edwards
├── archive/         # PDFs originais MAV
├── docs/           # Documentação do projeto
├── learning-paths/  # Trilhas de aprendizado (em desenvolvimento)
├── deepdive/       # Guias de aprofundamento (em desenvolvimento)
└── templates/      # Templates de projeto (em desenvolvimento)
```

### Status Atual (Jan 2025)
- ✅ Repositório reestruturado (v2.0)
- ✅ 4 livros convertidos para Markdown com alta qualidade
- ✅ PDFs dos livros mantidos como backup (decisão: manter)
- ⏳ 6 PDFs de exercícios MAV aguardando conversão
- ⏳ Sistema de metadados YAML pendente
- ⏳ Learning paths em desenvolvimento

### Ferramentas Instaladas
- **PyMuPDF4LLM**: Para conversão PDF → Markdown
- **OpenAI Whisper**: Para transcrição de áudio/vídeo
- **FFmpeg**: Para processamento de mídia
- **Python 3.9**: Com bibliotecas para processamento

### Próximas Prioridades
1. Converter 6 PDFs de exercícios MAV faltantes
2. Implementar sistema de metadados YAML
3. Criar learning paths
4. Desenvolver templates de projeto
5. Sistema de busca e indexação

## Comandos Úteis

### Para converter PDFs
```python
import pymupdf4llm
md_text = pymupdf4llm.to_markdown("arquivo.pdf")
```

### Para analisar copy de vídeos
```bash
python3 tools/video-copy-analyzer.py video.mp4 --model base
```

### Para buscar conteúdo específico
```bash
# Buscar em todos os arquivos Markdown
grep -r "termo" --include="*.md" .

# Buscar conceito específico
grep -r "big idea" modules/ exercises/ materials/
```

## Memória de Decisões Importantes

1. **PDFs dos livros**: Mantidos como backup (19.4MB total)
2. **Conversão**: PyMuPDF4LLM escolhido como ferramenta padrão
3. **Estrutura**: Pasta "pendente" removida, PDFs MAV movidos temporariamente
4. **Nomenclatura**: Padrão m[módulo]-[tema] mantido
5. **Integração**: Otimizada para uso com Claude Projects

---

*Última atualização: 18 de Janeiro de 2025*