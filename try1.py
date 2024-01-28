class User(db.Model):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    type_id: Mapped[int] = mapped_column(db.Integer, nullable=False) # FOREIGN KEY IN Dog_Breeder
    sender_id: Mapped[int] = mapped_column(db.Integer, nullable=False) 
    first_name: Mapped[str] = mapped_column(db.Text, nullable=False)
    last_name: Mapped[str] = mapped_column(db.Text, nullable=False)
    email: Mapped[str] = mapped_column(db.Text, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.Text, unique=True, nullable=False)

class Dog_Breeder(db.Model):
    __tablename__ = "Dog Breeder"
    type_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    dog_breeder_id: Mapped[int] = mapped_column(db.Integer, nullable=False) # FOREIGN KEY IN Breeder_profile
    first_name: Mapped[str] = mapped_column(db.Text, nullable=False)
    last_name: Mapped[str] = mapped_column(db.Text, nullable=False)
    professional_status: Mapped[str] = mapped_column(db.Text, nullable=False)
    phone_number: Mapped[int]=mapped_column(db.Integer, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.Text, unique=True, nullable=False)
    district: Mapped[str] = mapped_column(db.Text, nullable=False) 

class Breeder_profile(db.Model):
    __tablename__ = "Breeder Profile"
    dog_breeder_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    breeding_plan_id: Mapped[int] = mapped_column(db.Integer, nullable=False) # FOREIGN KEY IN Breeding_plan
    act_ant_strat: Mapped[str] = mapped_column(db.Text, nullable=False)
    background: Mapped[str] = mapped_column(db.Text, nullable=False)

class Breeding_plan(db.Model):
     __tablename__ = "Breeding Plan"
     breeding_plan_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)"
     