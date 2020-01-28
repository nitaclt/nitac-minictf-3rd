posts = [
  {content: "\\textrm{I'm gonna show you the FLAG:}", is_public: true, owner: "2ae96cac1e1659ef2231411ba36c8f77"},
  {content: "NITAC{wh4t_a_beaut1ful_f0rmu1a}", is_public: false, owner: "2ae96cac1e1659ef2231411ba36c8f77"},
  {content: "\\textrm{Oh, forgot to make it public haha}", is_public: true, owner: "2ae96cac1e1659ef2231411ba36c8f77"} 
]

posts.each do |po|
  Post.create po
end