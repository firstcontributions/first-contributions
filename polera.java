package practicasegundo;

public class polera {
    public String equipo;
    public int talla;
    public int precio;

    public polera(int talla, int precio, String equipo) {
        this.talla = talla;
        this.precio = precio;
        this.equipo = equipo;
    }

    public int getprecio() {
        return precio;
    }

    public void setprecio(int precio) {
        this.precio = precio;
    }
}