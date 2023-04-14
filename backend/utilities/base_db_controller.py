from backend import db

class DbController:
    def create_object(self, object: db.Model):
        self._add(object)
        self.commit()
        return object
    
    def delete_object(self, object: db.Model):
        self._delete(object)
        self.commit()
        return object
    
    def _add(self, object: db.Model):
        db.session.add(object)
    
    def _delete(self, object: db.Model):
        db.session.delete(object)
    
    @staticmethod
    def commit():
        db.session.commit()
    
    def get(self, **attrs):
        return self.model.query.filter_by(**attrs)
    
    def get_or_404(self, post_id):
        return self.model.query.get_or_404(post_id)
    
    def get_all(self):
        return self.model.query.all()