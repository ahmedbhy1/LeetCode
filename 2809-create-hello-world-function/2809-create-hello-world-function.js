/**
 * @return {Function}
 */


var createHelloWorld = () => {
    let a = ()=> {return  "Hello World";  }
    return a 
};
const f = createHelloWorld();

f(); // "Hello World"
