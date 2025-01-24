const test = (req, res) => {
    const files = req.files;
    res.json({ message: 'testing testing' });
};

export { test };