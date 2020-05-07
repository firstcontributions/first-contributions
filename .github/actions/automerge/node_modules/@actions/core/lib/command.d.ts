interface CommandProperties {
    [key: string]: any;
}
/**
 * Commands
 *
 * Command Format:
 *   ::name key=value,key=value::message
 *
 * Examples:
 *   ::warning::This is the message
 *   ::set-env name=MY_VAR::some value
 */
export declare function issueCommand(command: string, properties: CommandProperties, message: any): void;
export declare function issue(name: string, message?: string): void;
/**
 * Sanitizes an input into a string so it can be passed into issueCommand safely
 * @param input input to sanitize into a string
 */
export declare function toCommandValue(input: any): string;
export {};
