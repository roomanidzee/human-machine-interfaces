from flask_redis import FlaskRedis

def configure(app):
    """Configure Redis for system."""
    
    redis_client = FlaskRedis()
    redis_client.init_app(app)