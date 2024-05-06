/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    
    var current_value = init;
    
    return {
        increment : function(){
            return ++current_value;
        },
        decrement: function(){
            return --current_value;
        },
        reset: function(){
            current_value = init;
            return current_value;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */