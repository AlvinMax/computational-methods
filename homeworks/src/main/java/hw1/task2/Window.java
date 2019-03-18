package hw1.task2;

public class Window {
    private static final double EPS = 1e-6;
    private Double a, b, c;

    public Window(Double a, Double b, Double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public void setNext(Double d) {
        a = b;
        b = c;
        c = d;
    }

    public boolean isZero() {
        return isNear(0.0);
    }

    public boolean isNear(double near) {
        return Math.abs(a - near) < EPS && Math.abs(b - near) < EPS && Math.abs(c - near) < EPS;
    }

    public boolean isMonotonic() {
        return (a < b && b < c) || (c < b && b < a);
    }

    public boolean isZigZag() {
        return (a < b && c < b) || (a > b && c > b);
    }

    public boolean isDiverge() {
        return !isZero() && !isMonotonic() && !isZigZag();
    }
}
