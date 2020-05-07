declare module 'wasi' {
    interface WASIOptions {
        /**
         * An array of strings that the WebAssembly application will
         * see as command line arguments. The first argument is the virtual path to the
         * WASI command itself.
         */
        args?: string[];
        /**
         * An object similar to `process.env` that the WebAssembly
         * application will see as its environment.
         */
        env?: object;
        /**
         * This object represents the WebAssembly application's
         * sandbox directory structure. The string keys of `preopens` are treated as
         * directories within the sandbox. The corresponding values in `preopens` are
         * the real paths to those directories on the host machine.
         */
        preopens?: NodeJS.Dict<string>;

        /**
         * By default, WASI applications terminate the Node.js
         * process via the `__wasi_proc_exit()` function. Setting this option to `true`
         * causes `wasi.start()` to return the exit code rather than terminate the
         * process.
         * @default false
         */
        returnOnExit?: boolean;
    }

    class WASI {
        constructor(options?: WASIOptions);
        /**
         *
         * Attempt to begin execution of `instance` by invoking its `_start()` export.
         * If `instance` does not contain a `_start()` export, then `start()` attempts to
         * invoke the `__wasi_unstable_reactor_start()` export. If neither of those exports
         * is present on `instance`, then `start()` does nothing.
         *
         * `start()` requires that `instance` exports a [`WebAssembly.Memory`][] named
         * `memory`. If `instance` does not have a `memory` export an exception is thrown.
         */
        start(instance: object): void; // TODO: avoid DOM dependency until WASM moved to own lib.
        /**
         * Is an object that implements the WASI system call API. This object
         * should be passed as the `wasi_unstable` import during the instantiation of a
         * [`WebAssembly.Instance`][].
         */
        readonly wasiImport: NodeJS.Dict<any>; // TODO: Narrow to DOM types
    }
}
