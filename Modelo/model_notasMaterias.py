from controller import db
from sqlalchemy import func

class NotaMateria(db.Model):
    __tablename__ = 'notamateria'
    __table_args__ = {'extend_existing': True}
    

    notamateria_id = db.Column(db.Integer, primary_key=True)
    alumno_fk = db.Column(db.Integer)
    nombremateria = db.Column(db.String(2))
    notafinal = db.Column(db.Integer)

    def __init__(self,alumno,nombremateria,notafinal):
        self.alumno_fk=alumno,
        self.nombremateria=nombremateria,
        self.notafinal=notafinal         

    def save(self):
        db.session.add(self)
        db.session.commit()      

    def __repr__(self):
        return '<id {}>'.format(self.notamateria_id)

    @staticmethod
    def buscarNotasMaterias():
            #NotaMateria.query(func.count(User.id))
        return NotaMateria.query.order_by(NotaMateria.alumno_fk).all() 

    @staticmethod
    def buscarNotaMateriaByNotamateriaID(notamateria_id):
        return NotaMateria.query.filter_by(notamateria_id=notamateria_id).first()

    @staticmethod
    def getNotasMateriasByAlumnoID(id):
        return NotaMateria.query.filter_by(alumno_fk=id).order_by(NotaMateria.nombremateria).all()
        '''query = NotaMateria.query.filter(User.name.like('%ed')).order_by(User.id)'''
        '''return NotaMateria.query.filter_by(alumno_fk=id).first_or_404(description='No existe datos con el ID ={}'.format(id))'''
    #session.query(User).filter_by(name='jack').count() hacer esto para verificar si fue eliminado
    def delete(self):
        db.session.delete(self)
        db.session.commit() 

    def serializar(self):
        return {
            'notamateria_id': self.notamateria_id,
            'alumno': self.alumno_fk,
            'nombremateria':self.nombremateria,
            'notafinal':self.notafinal                   
        }
