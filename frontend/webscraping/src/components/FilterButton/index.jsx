import React from 'react';

function FilterButton({ button, filter }) {
    return (
        <div>
            {button.map((cat, i) => {
                return (
                    <button
                        key={i}
                        type="button"
                        data-mdb-ripple="true"
                        data-mdb-ripple-color="light"
                        onClick={() => filter(cat)}
                        className="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out m-2 "
                    >
                        {cat}
                    </button>
                );
            })}
        </div>
    );
}

export default FilterButton;
