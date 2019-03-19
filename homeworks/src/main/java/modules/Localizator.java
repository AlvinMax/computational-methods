package modules;

import modules.functions.Function;

import java.util.stream.Stream;

public interface Localizator<V> {

    /**
     *
     * @param fun
     * @param st
     * @param fn
     * @return
     */
    Stream<Segment<V>> localize(Function fun, V st, V fn);

    interface Segment<T> {
        T first();

        T secons();
    }
}
