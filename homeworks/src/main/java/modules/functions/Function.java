package modules.functions;

public interface Function<V> {

    void accept(V... args);

    V advance();
}
