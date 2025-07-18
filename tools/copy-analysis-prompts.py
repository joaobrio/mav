#!/usr/bin/env python3
"""
Copy Analysis Prompts - Prompts especializados para análise de copy

Este módulo fornece prompts estruturados para análise detalhada de copy
baseados nos 31 Secrets de Jim Edwards e outros frameworks de copywriting.

Autor: MAV System
Data: 2025-01-18
"""

# Prompts para análise estruturada
ANALYSIS_PROMPTS = {
    "headline_analysis": """
    Analise o headline/título desta copy:
    
    1. Ele captura atenção imediatamente?
    2. Promete um benefício claro?
    3. Cria curiosidade ou urgência?
    4. É específico ou vago?
    5. Usa palavras de poder (grátis, novo, descobrir, como)?
    
    Dê uma nota de 1-10 e sugira melhorias específicas.
    """,
    
    "reason_why": """
    Identifique e avalie o "reason why" (razão pela qual) nesta copy:
    
    1. Existe uma razão clara e convincente para comprar?
    2. A razão é lógica e emocional?
    3. É única ou diferenciada?
    4. Está bem posicionada na copy?
    
    Se não houver reason why claro, sugira um baseado no conteúdo.
    """,
    
    "fred_analysis": """
    Analise se a copy está direcionada ao F.R.E.D. (cliente ideal):
    
    F - Fears (Medos): Quais medos a copy aborda?
    R - Results (Resultados): Que resultados promete?
    E - Expectations (Expectativas): Que expectativas cria?
    D - Desires (Desejos): Quais desejos desperta?
    
    A copy fala diretamente com esses elementos?
    """,
    
    "bullet_formula": """
    Avalie os bullets (se houver) usando a Ultimate Bullet Formula:
    
    1. Começam com verbos de ação?
    2. Prometem benefícios específicos?
    3. Criam curiosidade?
    4. São concisos e impactantes?
    
    Reescreva 3 bullets usando a fórmula:
    [Verbo de ação] + [Benefício específico] + [Elemento de curiosidade]
    """,
    
    "emotional_triggers": """
    Identifique os gatilhos emocionais presentes:
    
    1. Medo de perder (FOMO)
    2. Desejo de ganhar
    3. Prova social
    4. Autoridade
    5. Reciprocidade
    6. Escassez
    7. Urgência
    
    Quais estão presentes? Quais poderiam ser adicionados?
    """,
    
    "sales_formula": """
    Identifique qual fórmula de vendas está sendo usada:
    
    1. AIDA (Atenção, Interesse, Desejo, Ação)
    2. PAS (Problema, Agitação, Solução)
    3. PASTOR (Problema, Amplificação, Story, Transformação, Oferta, Resposta)
    4. Outra estrutura
    
    A estrutura está completa? O que falta?
    """,
    
    "testimonial_power": """
    Avalie os depoimentos/testimonials:
    
    1. São específicos com números/resultados?
    2. Incluem nome completo e foto?
    3. Abordam objeções comuns?
    4. São relevantes para o público-alvo?
    5. Mostram transformação (antes/depois)?
    
    Como melhorar a credibilidade?
    """,
    
    "cta_strength": """
    Analise os Call-to-Actions (CTAs):
    
    1. São claros e específicos?
    2. Usam verbos de ação no imperativo?
    3. Criam urgência ou escassez?
    4. Estão bem posicionados?
    5. Há múltiplos CTAs ao longo da copy?
    
    Sugira CTAs mais fortes.
    """,
    
    "stealth_closes": """
    Identifique "stealth closes" (fechamentos sutis):
    
    1. Perguntas que assumem a venda
    2. Linguagem que pressupõe posse
    3. Visualização do futuro com o produto
    4. Comparações que favorecem a compra
    
    A copy usa esses elementos? Como implementar mais?
    """,
    
    "polish_checklist": """
    Checklist final de polimento (Secret #31):
    
    [ ] Headline poderoso e claro
    [ ] Lead que prende atenção
    [ ] Transições suaves entre seções
    [ ] Bullets escaneáveis
    [ ] Prova social forte
    [ ] Oferta irresistível
    [ ] Garantia que remove risco
    [ ] CTA urgente e claro
    [ ] P.S. que reforça benefício principal
    
    O que precisa ser melhorado?
    """
}

# Prompts para diferentes tipos de copy
COPY_TYPE_PROMPTS = {
    "vsl": """
    Análise específica para VSL (Video Sales Letter):
    
    1. O hook inicial prende nos primeiros 10 segundos?
    2. Há uma história envolvente?
    3. A revelação do produto está no timing certo?
    4. Os benefícios são demonstrados visualmente?
    5. Há urgência no final?
    """,
    
    "webinar": """
    Análise específica para Webinário:
    
    1. A promessa do webinário é clara?
    2. Há conteúdo de valor antes da venda?
    3. A transição para oferta é suave?
    4. Os bônus são relevantes?
    5. Há escassez genuína?
    """,
    
    "email": """
    Análise específica para Email:
    
    1. Subject line cria curiosidade?
    2. Preheader complementa o subject?
    3. O email tem um único objetivo?
    4. CTA está acima da dobra?
    5. É mobile-friendly?
    """,
    
    "landing_page": """
    Análise específica para Landing Page:
    
    1. Headline e subheadline estão alinhados?
    2. Há congruência com o anúncio?
    3. O formulário pede apenas o essencial?
    4. Benefícios superam features?
    5. Há elementos de trust?
    """
}

# Template para relatório de análise
REPORT_TEMPLATE = """
# Relatório de Análise de Copy

## 1. Resumo Executivo
- **Tipo de Copy**: {copy_type}
- **Score Geral**: {score}/100
- **Principais Forças**: {strengths}
- **Principais Fraquezas**: {weaknesses}

## 2. Análise Detalhada

### Headline e Hook
{headline_analysis}

### Estrutura e Fluxo
{structure_analysis}

### Elementos de Persuasão
{persuasion_analysis}

### Call-to-Action
{cta_analysis}

## 3. Recomendações Prioritárias

1. **Imediato** (Quick wins):
   {immediate_fixes}

2. **Curto Prazo** (1-2 semanas):
   {short_term}

3. **Longo Prazo** (Otimizações):
   {long_term}

## 4. Exemplos de Reescrita

### Headline Original:
> {original_headline}

### Headline Sugerido:
> {suggested_headline}

### Bullet Original:
> {original_bullet}

### Bullet Sugerido:
> {suggested_bullet}

## 5. Próximos Passos
{next_steps}
"""

def get_analysis_prompt(prompt_type, context=""):
    """
    Retorna um prompt específico com contexto
    
    Args:
        prompt_type: Tipo do prompt desejado
        context: Contexto adicional para personalizar o prompt
    
    Returns:
        Prompt formatado
    """
    base_prompt = ANALYSIS_PROMPTS.get(prompt_type, "")
    
    if context:
        return f"{base_prompt}\n\nContexto específico:\n{context}"
    
    return base_prompt

def get_copy_type_prompt(copy_type):
    """
    Retorna prompt específico para tipo de copy
    
    Args:
        copy_type: Tipo de copy (vsl, webinar, email, landing_page)
    
    Returns:
        Prompt específico
    """
    return COPY_TYPE_PROMPTS.get(copy_type, "")

def generate_analysis_report(analysis_data):
    """
    Gera relatório formatado com os dados da análise
    
    Args:
        analysis_data: Dicionário com dados da análise
    
    Returns:
        Relatório formatado
    """
    return REPORT_TEMPLATE.format(**analysis_data)

# Exemplos de uso
if __name__ == "__main__":
    # Exemplo de prompt para análise de headline
    print("=== Exemplo de Prompt para Headline ===")
    print(get_analysis_prompt("headline_analysis"))
    
    print("\n=== Exemplo de Prompt para VSL ===")
    print(get_copy_type_prompt("vsl"))
    
    # Exemplo de dados para relatório
    sample_data = {
        "copy_type": "VSL",
        "score": 75,
        "strengths": "Hook forte, história envolvente",
        "weaknesses": "CTA fraco, falta urgência",
        "headline_analysis": "Headline genérico, precisa mais especificidade",
        "structure_analysis": "Boa estrutura PAS, mas transições abruptas",
        "persuasion_analysis": "Usa prova social, mas falta autoridade",
        "cta_analysis": "CTA vago e sem urgência",
        "immediate_fixes": "- Reescrever CTA\n- Adicionar urgência",
        "short_term": "- Melhorar depoimentos\n- Adicionar garantia",
        "long_term": "- Testar diferentes hooks\n- A/B test headlines",
        "original_headline": "Descubra o Segredo do Sucesso",
        "suggested_headline": "Como 2.847 Empreendedores Triplicaram o Faturamento em 90 Dias",
        "original_bullet": "Aprenda técnicas de vendas",
        "suggested_bullet": "Domine a técnica secreta que fecha 73% mais vendas (página 47)",
        "next_steps": "1. Implementar CTAs urgentes\n2. Adicionar countdown timer\n3. Testar nova headline"
    }
    
    print("\n=== Exemplo de Relatório ===")
    print(generate_analysis_report(sample_data))