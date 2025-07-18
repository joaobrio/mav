# Workflow de Análise de Copy de Vídeos - Jim Edwards Framework

## Visão Geral

Este documento descreve o workflow completo para analisar copy de vídeos usando os 31 Secrets de Jim Edwards do livro "Copywriting Secrets".

## Ferramentas Disponíveis

### 1. OpenAI Whisper (✅ Instalado)
- **Status**: Disponível no sistema
- **Versão**: 20240930
- **Uso**: Transcrição automática de áudio/vídeo
- **Modelos**: tiny, base, small, medium, large

### 2. FFmpeg (✅ Instalado)
- **Status**: Disponível em `/opt/homebrew/bin/ffmpeg`
- **Uso**: Extração de áudio de vídeos
- **Formatos suportados**: MP4, AVI, MOV, MKV, etc.

### 3. Scripts Customizados (✅ Criados)
- **video-copy-analyzer.py**: Análise automatizada completa
- **copy-analysis-prompts.py**: Prompts estruturados para análise detalhada

## Workflow Recomendado

### Fase 1: Preparação

1. **Verificar formato do vídeo**
   ```bash
   ffmpeg -i seu_video.mp4 2>&1 | grep Duration
   ```

2. **Escolher modelo Whisper apropriado**
   - **tiny/base**: Vídeos curtos (< 10 min), análise rápida
   - **small/medium**: Vídeos médios (10-30 min), melhor precisão
   - **large**: Vídeos longos ou copy complexa, máxima precisão

### Fase 2: Transcrição

1. **Usando o script automatizado**
   ```bash
   python3 /Users/joaorovere/Documents/GitHub/mav/tools/video-copy-analyzer.py seu_video.mp4 --model base
   ```

2. **Transcrição manual com Whisper**
   ```bash
   # Extrair áudio primeiro
   ffmpeg -i video.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 audio.wav
   
   # Transcrever
   whisper audio.wav --language pt --model base
   ```

### Fase 3: Análise Automatizada

O script `video-copy-analyzer.py` analisa automaticamente:

1. **Elementos Essenciais**
   - Headline/Hook inicial
   - Reason Why (Por que comprar)
   - Bullets e benefícios
   - Testimonials/Prova social
   - Call-to-Actions
   - Foco no cliente vs. produto
   - Gatilhos emocionais
   - Estrutura de vendas

2. **Score de Qualidade**
   - 80-100: Excelente copy
   - 60-79: Boa copy com melhorias
   - 40-59: Copy mediana
   - 0-39: Copy fraca

### Fase 4: Análise Aprofundada

Use os prompts do `copy-analysis-prompts.py` para análise detalhada:

```python
from copy_analysis_prompts import get_analysis_prompt

# Analisar headline
prompt = get_analysis_prompt("headline_analysis")
# Use com Claude ou GPT para análise

# Analisar estrutura F.R.E.D.
prompt = get_analysis_prompt("fred_analysis")
```

### Fase 5: Relatório e Recomendações

O relatório gerado automaticamente inclui:

1. **Resumo Executivo**
   - Score geral
   - Elementos encontrados
   - Principais problemas

2. **Análise Detalhada**
   - Cada elemento com referência aos Secrets
   - Qualidade e quantidade
   - Comparação com best practices

3. **Recomendações Prioritizadas**
   - Melhorias imediatas
   - Otimizações de médio prazo
   - Testes A/B sugeridos

## Implementação Prática

### Exemplo 1: VSL (Video Sales Letter)

```bash
# Analisar VSL de vendas
python3 video-copy-analyzer.py minha_vsl.mp4 --model small

# Resultado esperado:
# - Hook forte nos primeiros 10 segundos
# - História que cria conexão emocional
# - Transição suave para oferta
# - Multiple CTAs com urgência
# - Score > 70
```

### Exemplo 2: Webinário

```bash
# Analisar webinário de 45 minutos
python3 video-copy-analyzer.py webinario.mp4 --model medium

# Pontos de atenção:
# - Promessa clara no início
# - Conteúdo de valor antes da pitch
# - Stack de bônus bem apresentado
# - Escassez e urgência genuínas
```

### Exemplo 3: Video Ad

```bash
# Analisar anúncio curto
python3 video-copy-analyzer.py ad_facebook.mp4 --model tiny

# Foco em:
# - Hook nos primeiros 3 segundos
# - Benefício principal claro
# - CTA único e direto
# - Congruência com landing page
```

## Integração com MAV

### 1. Análise de Concorrentes
Use o workflow para analisar vídeos de concorrentes:
- Identificar elementos de sucesso
- Encontrar gaps na comunicação
- Criar swipe file organizado

### 2. Otimização Contínua
- Analisar próprios vídeos antes de publicar
- Comparar scores ao longo do tempo
- Testar diferentes abordagens

### 3. Templates e Padrões
- Criar biblioteca de headlines que funcionam
- Documentar bullets de alta conversão
- Catalogar CTAs efetivos

## Comandos Úteis

```bash
# Instalar/Atualizar Whisper
python3 -m pip install -U openai-whisper

# Verificar instalação
python3 -c "import whisper; print(whisper.__version__)"

# Processar múltiplos vídeos
for video in *.mp4; do
    python3 video-copy-analyzer.py "$video" --model base
done

# Extrair apenas áudio para análise manual
ffmpeg -i video.mp4 -vn -c:a copy audio.m4a
```

## Troubleshooting

### Problema: Whisper muito lento
**Solução**: Use modelo menor ou processe em partes
```bash
# Dividir vídeo em partes de 10 minutos
ffmpeg -i input.mp4 -c copy -map 0 -segment_time 600 -f segment output%03d.mp4
```

### Problema: Transcrição imprecisa
**Solução**: 
1. Melhorar qualidade do áudio
2. Usar modelo maior
3. Especificar idioma correto

### Problema: Memória insuficiente
**Solução**: Use modelo tiny ou base, ou processe em cloud

## Próximos Passos

1. **Automação Completa**
   - Criar pipeline para processar vídeos automaticamente
   - Integrar com ferramentas de IA para sugestões

2. **Dashboard de Análise**
   - Visualizar scores ao longo do tempo
   - Comparar performance entre vídeos
   - Identificar padrões de sucesso

3. **Integração com IA**
   - Usar Claude/GPT para sugestões de melhoria
   - Gerar variações de copy automaticamente
   - A/B testing automatizado

## Recursos Adicionais

- **Livro Completo**: `/references/jim-edwards/copywriting-secrets-complete.md`
- **31 Secrets Reference**: Consulte o livro para detalhes de cada secret
- **Exemplos de Copy**: Crie seu próprio swipe file com vídeos analisados

---

**Nota**: Este workflow foi otimizado para o ambiente macOS com as ferramentas já instaladas. Para outros sistemas, ajuste os caminhos conforme necessário.