"""
文本處理器 - 負責情感分析、關鍵詞提取等功能
"""

import logging
from typing import Dict, List

logger = logging.getLogger('news_automation')

class TextProcessor:
    """文本處理器"""
    
    def __init__(self):
        logger.info("文本處理器初始化完成")
        print("✅ 文本處理器已創建")
    
    def analyze_sentiment(self, text: str) -> Dict:
        """分析文本情感"""
        if not text:
            return {
                'score': 0.0,
                'label': 'neutral',
                'confidence': 0.0
            }
        
        # 簡單的情感分析
        positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful']
        negative_words = ['bad', 'terrible', 'awful', 'horrible', 'worst']
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            label = 'positive'
            score = 0.5
        elif negative_count > positive_count:
            label = 'negative'
            score = -0.5
        else:
            label = 'neutral'
            score = 0.0
            
        return {
            'score': score,
            'label': label,
            'confidence': abs(score)
        }
    
    def extract_keywords(self, text: str, max_keywords: int = 10) -> List[str]:
        """提取關鍵詞"""
        if not text:
            return []
        
        import re
        words = re.findall(r'\b\w{3,}\b', text.lower())
        
        # 移除停用詞
        stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        keywords = [word for word in words if word not in stop_words]
        
        # 統計詞頻
        word_count = {}
        for word in keywords:
            word_count[word] = word_count.get(word, 0) + 1
        
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        return [word for word, count in sorted_words[:max_keywords]]
    
    def process_article_content(self, article_data: Dict) -> Dict:
        """處理文章內容"""
        content = article_data.get('content', '')
        title = article_data.get('title', '')
        
        full_text = f"{title}. {content}"
        
        return {
            'sentiment': self.analyze_sentiment(full_text),
            'keywords': self.extract_keywords(full_text),
            'word_count': len(content.split()) if content else 0,
            'reading_time': max(1, len(content.split()) // 200) if content else 0
        }
