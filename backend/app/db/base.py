from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    """
    This is the base class all your database models will inherit from.
    It should not contain any column definitions itself.
    """
    pass  # Keep the class body empty, except for the function below

    # --- THIS IS THE AUTOMATIC NAMING SNIPPET ---
    @declared_attr
    def __tablename__(cls) -> str:
        """
        This automatically generates a table name for any class
        that inherits from this Base.
        
        Example:
        - Class `User` becomes table `users`
        - Class `Doctor` becomes table `doctors`
        - Class `Prescription` becomes table `prescriptions`
        """
        return cls.__name__.lower() + "s"
    # ---------------------------------------------