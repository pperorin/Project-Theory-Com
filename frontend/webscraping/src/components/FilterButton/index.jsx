import React from "react";

function FilterButton({ button, filter }) {
  return (
    <div>
      {button.map((cat, i) => {
            return (
                <>
                {/* <div class="flex space-x-2 justify-left"> */}
                <button
    type="button"
    data-mdb-ripple="true"
    data-mdb-ripple-color="light"
    onClick={() => filter(cat)}
    class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out m-2 "
  >{cat}</button>
                {/* </div> */}
                </>
            );

        // return <button className="border-4" type="button" onClick={() => filter(cat)}>{cat}</button>
      })}
    </div>
  );
}

export default FilterButton;