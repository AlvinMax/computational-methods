package hw1.task2;

import java.util.Iterator;
import java.util.function.Function;

public class SimpleIterationsImpl implements SimpleIterations {

    private static final double EPS = 1e-5;

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
        for (int i = 0; i < 100000; i++) {
            it.next();
        }

        final Window window = new Window(it.next(), it.next(), it.next());
        return f.apply(window);
    }


}
