from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime, timezone  # 新增這行
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    news_articles = relationship("NewsArticle", back_populates="author")


class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), index=True)
    content = Column(Text)
    source_url = Column(String(500))
    author_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    published_at = Column(DateTime(timezone=True))
    scraped_at = Column(DateTime(timezone=True), server_default=func.now())
    sentiment_score = Column(Float)
    is_published = Column(Boolean, default=False)

    author = relationship("User", back_populates="news_articles")
    category = relationship("Category", back_populates="articles")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    articles = relationship("NewsArticle", back_populates="category")


class ScheduledTask(Base):
    __tablename__ = "scheduled_tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String(100), index=True)
    task_type = Column(String(50))
    schedule_expression = Column(String(100))
    last_run = Column(DateTime(timezone=True))
    next_run = Column(DateTime(timezone=True))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    @property
    def time_until_next_run(self):
        """Calculate time until next scheduled run."""
        if self.next_run:
            now = datetime.now(timezone.utc)
            return self.next_run.replace(tzinfo=timezone.utc) - now
        return None
    
    def set_next_run_time(self, hours_from_now=1):
        """Set the next run time to specified hours from now."""
        from datetime import timedelta
        self.next_run = datetime.now(timezone.utc) + timedelta(hours=hours_from_now)