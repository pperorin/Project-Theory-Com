import React, { useState } from 'react';
import { serviceDropdown } from './NavItems';
import { Link } from 'react-router-dom';
import './Dropdown.css';

function Dropdown() {
    const [dropdown, setDropdown] = useState(false);

    return (
        <div className="dd-container">
            <ul
                className={dropdown ? 'services-submenu clicked' : 'services-submenu'}
                onClick={() => setDropdown(!dropdown)}
            >
                {serviceDropdown.map((item) => {
                    return (
                        <li key={item.id}>
                            <Link to={item.path} className={item.cName} onClick={() => setDropdown(false)}>
                                {item.icon}
                                {item.title}
                            </Link>
                        </li>
                    );
                })}
            </ul>
        </div>
    );
}

export default Dropdown;
