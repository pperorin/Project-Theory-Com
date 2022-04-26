import { FaBars, FaMouse, FaHeadset, FaKeyboard } from 'react-icons/fa';
export const navItems = [
    {
        id: 1,
        title: 'Home',
        path: '/',
        cName: 'nav-item',
        icon: <FaBars />,
    },
];

export const serviceDropdown = [
    {
        id: 1,
        title: 'Mouse',
        path: '/?search=mouse',
        cName: 'submenu-item',
        icon: <FaMouse />,
    },
    {
        id: 2,
        title: 'Headgear',
        path: '/?search=headgear',
        cName: 'submenu-item',
        icon: <FaHeadset />,
    },
    {
        id: 3,
        title: 'Keyboard',
        path: '/?search=keyboard',
        cName: 'submenu-item',
        icon: <FaKeyboard />,
    },
];
