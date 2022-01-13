defmodule FrameServerTest do
  use ExUnit.Case
  doctest FrameServer

  test "greets the world" do
    assert FrameServer.hello() == :world
  end
end
