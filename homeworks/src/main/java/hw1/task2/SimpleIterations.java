package hw1.task2;

import java.util.Iterator;
import java.util.List;
import java.util.function.Function;

public interface SimpleIterations {
    Iterator<Double> getIterator(Function<Double, Double> f, double start);
    boolean checkR(double r, double start, Function<Window, Boolean> f);
    double[] getValues(double r, double start, int N);
}
