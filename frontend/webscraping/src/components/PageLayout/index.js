import NavigationBar from './NavigationBar';

const PageLayout = (props) => {
    const { children } = props;

    return (
        <>
            <NavigationBar />
            {children}
        </>
    );
};

export default PageLayout;
