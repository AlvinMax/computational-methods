package hw1.task2;

import java.util.Iterator;
import java.util.function.Function;

public class SimpleIterationsImpl implements SimpleIterations {
    private static final int ITERATIONS = 100000;

    @Override
    public Iterator<Double> getIterator(Function<Double, Double> f, double start) {
        return new Iterator<Double>() {
            private double pos = start;

            @Override
            public boolean hasNext() {
                return true;
            }

            @Override
            public Double next() {
                double ret = pos;
                pos = f.apply(pos);
                return ret;
            }
        };
    }

    @Override
    public boolean checkR(double r, double start, Function<Window, Boolean> f) {
        final Function<Double, Double> rFunction = x -> r * x * (1 - x);
        final Iterator <Double> it = getIterator(rFunction, start);
        for (int i = 0; i < ITERATIONS; i++) {
            it.next();
        }

        final Window window = new Window(it.next(), it.next(), it.next());
        return f.apply(window);
    }

    @Override
    public double[] getValues(double r, double start, int N) {
        final Function<Double, Double> rFunction = x -> r * x * (1 - x);
        final Iterator<Double> it = getIterator(rFunction, start);
        double[] values = new double[N];
        for (int i = 0; i < N; i++) {
            values[i] = it.next();
        }
        return values;
    }


}
