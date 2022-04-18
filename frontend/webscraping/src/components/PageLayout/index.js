import NavigationBar from './NavigationBar';

const PageLayout = (props) => {
    const { children } = props;

    return (
        <>
            <NavigationBar />
            <div className="container mx-auto pt-8 px-8">{children}</div>
        </>
    );
};

export default PageLayout;
