package hw1.task2;

import org.math.plot.Plot2DPanel;

import javax.swing.*;
import java.util.function.Function;

public class Main {

    private static final double EPS = 1e-5;
    private static final SimpleIterations SI = new SimpleIterationsImpl();

    private static double binarySearch(double l, double r, double start, int type) {
        if (Math.abs(l - r) < EPS) return r;
        double m = (l + r) / 2;

        Function<Window, Boolean> f = w -> false;
        if (type == 1) {
            f = Window::isZero;
        }
        if (type == 2) {
            f = w -> w.isMonotonic() && w.isNear(1 - 1/m);
        }
        if (type == 3) {
            f = w -> w.isZigZag() && w.isNear(1 - 1/m);
        }

        if (SI.checkR(m, start, f)) {
            return binarySearch(m, r, start, type);
        } else {
            return binarySearch(l, m, start, type);
        }
    }

    private static void createPlot(double r, double start, int N, String nameOfPlot) {
        double[] x = new double[N];
        for (int i = 0; i < N; i++) {
            x[i] = (double) i;
        }
;
        double[] y = SI.getValues(r, start, N);

        // create your PlotPanel (you can use it as a JPanel)
        Plot2DPanel plot = new Plot2DPanel();

        // add a line plot to the PlotPanel
        plot.addLinePlot("my plot", x, y);

        // put the PlotPanel in a JFrame, as a JPanel
        JFrame frame = new JFrame(nameOfPlot);
        frame.setContentPane(plot);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        final double left = 0.0;
        final double right = 1000.0;
        final double start = .5;

        final double r1 = binarySearch(left, right, start, 1);
        final double r2 = binarySearch(r1, right, start, 2);
        final double r3 = binarySearch(r2, right, start, 3);

        System.out.println("r\' = " + r1);
        System.out.println("r\'\' = " + r2);
        System.out.println("r\'\'\' = " + r3);

        createPlot(r1 - 0.5, start, 50, "Сходимость к нулю");
        createPlot(r1 + 0.5, start, 50, "Монотонная к 1-1/r");
        createPlot(r3 - 0.1, start, 50, "Зигзагообразная к 1-1/r");
        createPlot(r3 + 0.5, start, 50, "Расходимость");
    }
}
