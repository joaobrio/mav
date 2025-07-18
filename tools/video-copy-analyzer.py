#!/usr/bin/env python3
"""
Video Copy Analyzer - Análise de Copy de Vídeos usando os 31 Secrets de Jim Edwards

Este script permite:
1. Transcrever áudio de vídeos usando OpenAI Whisper
2. Analisar a copy transcrita usando os princípios de Jim Edwards
3. Gerar relatórios detalhados sobre a eficácia da copy

Autor: MAV System
Data: 2025-01-18
"""

import os
import sys
import json
import argparse
import whisper
import tempfile
import subprocess
from datetime import datetime
from pathlib import Path

# 31 Secrets de Jim Edwards para análise
JIM_EDWARDS_SECRETS = {
    1: "WHAT IS COPYWRITING?",
    2: "ONE MAN'S JOURNEY WITH SALES COPY",
    3: "WITHOUT A STRONG WHY, PEOPLE DON'T BUY",
    4: "NOBODY CARES ABOUT YOU IN YOUR SALES COPY",
    5: "THE MOST VALUABLE SKILL YOU'LL EVER LEARN",
    6: "THE #1 SINGLE MOST IMPORTANT PIECE OF SALES COPY EVER!",
    7: "IT'S NEVER 'ONE SIZE FITS ALL'",
    8: "MEET F.R.E.D. (YOUR IDEAL CUSTOMER)",
    9: "THE ULTIMATE BULLET FORMULA",
    10: "WHAT REALLY SELLS PEOPLE (IT'S NOT WHAT YOU THINK)",
    11: "WHY GOOD ENOUGH MAKES YOU (AND KEEPS YOU) POOR!",
    12: "DON'T REINVENT THE WHEEL—GREAT COPY LEAVES CLUES",
    13: "IT'S ALL ABOUT THEM—NEVER ABOUT YOU",
    14: "WHAT TO DO IF YOU DON'T HAVE ANY TESTIMONIALS YET",
    15: "3 SALES FORMULAS THAT NEVER FAIL",
    16: "IT'S ALL ICE CREAM, BUT WHAT FLAVOR SHOULD I CHOOSE?",
    17: "HOW TO WRITE AN AMAZING SALES LETTER—FAST",
    18: "HOW TO WRITE KILLER EMAIL TEASERS—FAST",
    19: "THE HARDEST DRAFT YOU'LL EVER WRITE",
    20: "MAKE 'EM MORE THIRSTY",
    21: "LOVE ME; HATE ME. THERE'S NO MONEY IN THE MIDDLE",
    22: "'OH DAMN—I GOT TO HAVE THAT!'",
    23: "PUT LIPSTICK ON THE PIG",
    24: "SHOULD I JOIN THE DARK SIDE?",
    25: "'STEALTH' CLOSES—THE SECRET TO SELLING WITHOUT SELLING",
    26: "THE HIRED GUN",
    27: "THE MAGIC DESK",
    28: "THE ONE AND ONLY PURPOSE OF AN ONLINE AD",
    29: "YOU CAN'T CATCH FISH WITHOUT A HOOK",
    30: "CREATE YOUR OWN SWIPE FILE",
    31: "POLISH YOUR SALES COPY"
}

# Elementos-chave para análise
COPY_ELEMENTS = {
    "headline": {
        "description": "Título principal que captura atenção",
        "secrets": [6, 28, 29]
    },
    "reason_why": {
        "description": "Razão clara do porquê comprar",
        "secrets": [3, 10]
    },
    "bullets": {
        "description": "Lista de benefícios em formato bullet",
        "secrets": [9]
    },
    "testimonials": {
        "description": "Depoimentos e prova social",
        "secrets": [14]
    },
    "call_to_action": {
        "description": "Chamada para ação clara",
        "secrets": [25, 29]
    },
    "audience_focus": {
        "description": "Foco no cliente, não no produto",
        "secrets": [4, 8, 13]
    },
    "emotional_triggers": {
        "description": "Gatilhos emocionais e desejo",
        "secrets": [10, 20, 21, 22]
    },
    "structure": {
        "description": "Estrutura e fórmulas de vendas",
        "secrets": [15, 17, 18]
    }
}

class VideoCopyAnalyzer:
    def __init__(self, model_size="base"):
        """
        Inicializa o analisador de copy
        
        Args:
            model_size: Tamanho do modelo Whisper (tiny, base, small, medium, large)
        """
        print(f"Carregando modelo Whisper '{model_size}'...")
        self.whisper_model = whisper.load_model(model_size)
        self.analysis_results = {}
        
    def extract_audio(self, video_path, output_path=None):
        """
        Extrai áudio de vídeo usando ffmpeg
        
        Args:
            video_path: Caminho do vídeo
            output_path: Caminho de saída (opcional)
            
        Returns:
            Caminho do arquivo de áudio extraído
        """
        if output_path is None:
            output_path = tempfile.mktemp(suffix=".wav")
            
        print(f"Extraindo áudio de {video_path}...")
        cmd = [
            "ffmpeg",
            "-i", video_path,
            "-vn",  # Sem vídeo
            "-acodec", "pcm_s16le",  # Codec de áudio
            "-ar", "16000",  # Taxa de amostragem
            "-ac", "1",  # Mono
            "-y",  # Sobrescrever
            output_path
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"Áudio extraído para: {output_path}")
            return output_path
        except subprocess.CalledProcessError as e:
            print(f"Erro ao extrair áudio: {e}")
            return None
            
    def transcribe(self, audio_path):
        """
        Transcreve áudio usando Whisper
        
        Args:
            audio_path: Caminho do arquivo de áudio
            
        Returns:
            Texto transcrito
        """
        print(f"Transcrevendo áudio...")
        result = self.whisper_model.transcribe(audio_path, language="pt")
        
        # Salva transcrição com timestamps
        self.transcription = result
        return result["text"]
        
    def analyze_copy_elements(self, text):
        """
        Analisa elementos de copy no texto
        
        Args:
            text: Texto a analisar
            
        Returns:
            Dicionário com análise
        """
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "text_length": len(text),
            "word_count": len(text.split()),
            "elements_found": {},
            "recommendations": [],
            "score": 0
        }
        
        # Análise de headline (primeiras palavras)
        first_words = text[:200].strip()
        if any(trigger in first_words.lower() for trigger in ["descubra", "como", "você", "grátis", "novo"]):
            analysis["elements_found"]["headline"] = {
                "found": True,
                "quality": "good",
                "text": first_words
            }
            analysis["score"] += 10
        else:
            analysis["recommendations"].append(
                "Headline fraca - considere usar gatilhos como 'Como', 'Descubra', ou benefício claro"
            )
            
        # Análise de reason why
        reason_triggers = ["porque", "razão", "motivo", "por isso", "já que"]
        if any(trigger in text.lower() for trigger in reason_triggers):
            analysis["elements_found"]["reason_why"] = {
                "found": True,
                "quality": "present"
            }
            analysis["score"] += 15
        else:
            analysis["recommendations"].append(
                "Falta 'reason why' claro - explique POR QUE o cliente deve comprar"
            )
            
        # Análise de bullets
        if text.count("•") > 3 or text.count("-") > 5 or text.count("✓") > 2:
            analysis["elements_found"]["bullets"] = {
                "found": True,
                "count": max(text.count("•"), text.count("-"), text.count("✓"))
            }
            analysis["score"] += 10
        else:
            analysis["recommendations"].append(
                "Use bullets para listar benefícios de forma clara e escaneável"
            )
            
        # Análise de testimonials
        testimonial_triggers = ["depoimento", "cliente", "resultado", "consegui", "mudou minha vida"]
        if any(trigger in text.lower() for trigger in testimonial_triggers):
            analysis["elements_found"]["testimonials"] = {
                "found": True
            }
            analysis["score"] += 15
            
        # Análise de call to action
        cta_triggers = ["clique", "compre", "adquira", "garanta", "aproveite", "inscreva", "baixe"]
        cta_count = sum(1 for trigger in cta_triggers if trigger in text.lower())
        if cta_count > 0:
            analysis["elements_found"]["call_to_action"] = {
                "found": True,
                "count": cta_count,
                "quality": "strong" if cta_count > 2 else "weak"
            }
            analysis["score"] += 20
        else:
            analysis["recommendations"].append(
                "CRÍTICO: Falta call-to-action claro - diga exatamente o que o cliente deve fazer"
            )
            
        # Análise de foco no cliente
        you_count = text.lower().count("você") + text.lower().count("seu") + text.lower().count("sua")
        i_count = text.lower().count("eu ") + text.lower().count("meu") + text.lower().count("minha")
        
        if you_count > i_count * 2:
            analysis["elements_found"]["audience_focus"] = {
                "found": True,
                "ratio": f"{you_count}:{i_count}",
                "quality": "excellent"
            }
            analysis["score"] += 20
        else:
            analysis["recommendations"].append(
                f"Muito foco em você ({i_count}x) vs cliente ({you_count}x) - inverta essa proporção"
            )
            
        # Análise de gatilhos emocionais
        emotional_triggers = ["sonho", "medo", "frustração", "desejo", "transformar", "mudar", "resolver"]
        emotional_count = sum(1 for trigger in emotional_triggers if trigger in text.lower())
        if emotional_count > 2:
            analysis["elements_found"]["emotional_triggers"] = {
                "found": True,
                "count": emotional_count
            }
            analysis["score"] += 10
            
        # Score final
        analysis["score_interpretation"] = self._interpret_score(analysis["score"])
        
        return analysis
        
    def _interpret_score(self, score):
        """Interpreta o score da análise"""
        if score >= 80:
            return "Excelente copy - implementa maioria dos princípios de Jim Edwards"
        elif score >= 60:
            return "Boa copy - alguns elementos faltando"
        elif score >= 40:
            return "Copy mediana - precisa melhorias significativas"
        else:
            return "Copy fraca - revisar estrutura e elementos essenciais"
            
    def generate_report(self, video_path, transcription, analysis):
        """
        Gera relatório completo da análise
        
        Args:
            video_path: Caminho do vídeo analisado
            transcription: Transcrição completa
            analysis: Resultados da análise
            
        Returns:
            Caminho do relatório gerado
        """
        report_name = f"copy_analysis_{Path(video_path).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        report_path = Path(video_path).parent / report_name
        
        report_content = f"""# Análise de Copy - {Path(video_path).name}

## Resumo Executivo

- **Data da Análise**: {analysis['timestamp']}
- **Duração do Vídeo**: {self.transcription.get('duration', 'N/A')} segundos
- **Palavras Transcritas**: {analysis['word_count']}
- **Score Geral**: {analysis['score']}/100
- **Avaliação**: {analysis['score_interpretation']}

## Elementos de Copy Encontrados

"""
        
        for element, details in analysis['elements_found'].items():
            element_info = COPY_ELEMENTS[element]
            report_content += f"### {element.replace('_', ' ').title()}\n"
            report_content += f"*{element_info['description']}*\n\n"
            report_content += f"**Status**: {'✅ Encontrado' if details.get('found') else '❌ Não encontrado'}\n"
            
            if 'quality' in details:
                report_content += f"**Qualidade**: {details['quality']}\n"
            if 'count' in details:
                report_content += f"**Quantidade**: {details['count']}\n"
            if 'ratio' in details:
                report_content += f"**Proporção**: {details['ratio']}\n"
                
            # Secrets relacionados
            report_content += f"\n**Secrets Relacionados**: "
            for secret_num in element_info['secrets']:
                report_content += f"\n- Secret #{secret_num}: {JIM_EDWARDS_SECRETS[secret_num]}"
            report_content += "\n\n"
            
        # Recomendações
        if analysis['recommendations']:
            report_content += "## 🎯 Recomendações de Melhoria\n\n"
            for i, rec in enumerate(analysis['recommendations'], 1):
                report_content += f"{i}. {rec}\n"
                
        # Transcrição
        report_content += f"\n## Transcrição Completa\n\n```\n{transcription}\n```\n"
        
        # Salvar relatório
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
            
        return report_path
        
    def analyze_video(self, video_path):
        """
        Pipeline completo de análise de vídeo
        
        Args:
            video_path: Caminho do vídeo
            
        Returns:
            Caminho do relatório gerado
        """
        # 1. Extrair áudio
        audio_path = self.extract_audio(video_path)
        if not audio_path:
            return None
            
        # 2. Transcrever
        transcription = self.transcribe(audio_path)
        
        # 3. Analisar copy
        analysis = self.analyze_copy_elements(transcription)
        
        # 4. Gerar relatório
        report_path = self.generate_report(video_path, transcription, analysis)
        
        # 5. Limpar arquivo temporário
        if audio_path.startswith(tempfile.gettempdir()):
            os.remove(audio_path)
            
        print(f"\n✅ Análise completa! Relatório salvo em: {report_path}")
        print(f"Score: {analysis['score']}/100 - {analysis['score_interpretation']}")
        
        return report_path


def main():
    parser = argparse.ArgumentParser(
        description="Analisa copy de vídeos usando os 31 Secrets de Jim Edwards"
    )
    parser.add_argument("video", help="Caminho do vídeo para analisar")
    parser.add_argument(
        "--model", 
        default="base", 
        choices=["tiny", "base", "small", "medium", "large"],
        help="Tamanho do modelo Whisper (default: base)"
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.video):
        print(f"Erro: Arquivo não encontrado: {args.video}")
        sys.exit(1)
        
    # Executar análise
    analyzer = VideoCopyAnalyzer(model_size=args.model)
    analyzer.analyze_video(args.video)


if __name__ == "__main__":
    main()